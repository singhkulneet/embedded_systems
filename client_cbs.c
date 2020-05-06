//*****************************************************************************
//
//! \addtogroup mqtt_server
//! @{
//
//*****************************************************************************
/* Standard includes                                                         */
#include <stdlib.h>

/* Kernel (Non OS/Free-RTOS/TI-RTOS) includes                                */
#include "pthread.h"
#include "mqueue.h"

/* Common interface includes                                                 */
#include "uart_term.h"

/* Application includes                                                      */
#include "client_cbs.h"
#include "cJSON.h"
#include "jsmn.h"
#include "json_parse.h"


extern bool gResetApplication;

//*****************************************************************************
//                          LOCAL DEFINES
//*****************************************************************************
#define APP_PRINT               Report

#define OS_WAIT_FOREVER         (0xFFFFFFFF)
#define OS_NO_WAIT              (0)
#define OS_OK                   (0)

#define MQTTClientCbs_ConnackRC(data) (data & 0xff) 
/**< CONNACK: Return Code (LSB) */

//*****************************************************************************
//                 GLOBAL VARIABLES
//*****************************************************************************

/* Message Queue                                                              */
extern mqd_t g_PBQueue;
extern char *topic[];
struct client_info client_info_table[MAX_CONNECTION];

//*****************************************************************************
//                 Queue external function
//*****************************************************************************
extern int32_t MQTT_SendMsgToQueue(struct msgQueue *queueElement);

//****************************************************************************
//                      CLIENT CALLBACKS
//****************************************************************************

//*****************************************************************************
//
//! Callback in case of various event (for clients connection with remote
//! broker)
//!
//! \param[in]  event       - is a event occurred
//! \param[in]  metaData    - is the pointer for the message buffer
//!                           (for this event)
//! \param[in]  metaDateLen - is the length of the message buffer
//! \param[in]  data        - is the pointer to the buffer for data
//!                           (for this event)
//! \param[in]  dataLen     - is the length of the buffer data
//!
//! return none
//
//*****************************************************************************
void MqttClientCallback(int32_t event,
                        void * metaData,
                        uint32_t metaDateLen,
                        void *data,
                        uint32_t dataLen)
{
    int32_t i = 0;

    switch((MQTTClient_EventCB)event)
    {
    case MQTTClient_OPERATION_CB_EVENT:
    {
        switch(((MQTTClient_OperationMetaDataCB *)metaData)->messageType)
        {
        case MQTTCLIENT_OPERATION_CONNACK:
        {
            uint16_t *ConnACK = (uint16_t*) data;
            APP_PRINT("CONNACK:\n\r");
            /* Check if Conn Ack return value is Success (0) or       */
            /* Error - Negative value                                 */
            if(0 == (MQTTClientCbs_ConnackRC(*ConnACK)))
            {
                APP_PRINT("Connection Success\n\r");
            }
            else
            {
                APP_PRINT("Connection Error: %d\n\r", *ConnACK);
            }
            break;
        }

        case MQTTCLIENT_OPERATION_EVT_PUBACK:
        {
            char *PubAck = (char *) data;
            APP_PRINT("PubAck:\n\r");
            APP_PRINT("%s\n\r", PubAck);
            break;
        }

        case MQTTCLIENT_OPERATION_SUBACK:
        {
            APP_PRINT("Sub Ack:\n\r");
            APP_PRINT("Granted QoS Levels are:\n\r");
            for(i = 0; i < dataLen; i++)
            {
                APP_PRINT("%s :QoS %d\n\r", topic[i],
                          ((unsigned char*) data)[i]);
            }
            break;
        }

        case MQTTCLIENT_OPERATION_UNSUBACK:
        {
            char *UnSub = (char *) data;
            APP_PRINT("UnSub Ack \n\r");
            APP_PRINT("%s\n\r", UnSub);
            break;
        }

        default:
            break;
        }
        break;
    }
    case MQTTClient_RECV_CB_EVENT:
    {
        MQTTClient_RecvMetaDataCB *recvMetaData =
            (MQTTClient_RecvMetaDataCB *)metaData;
        uint32_t bufSizeReqd = 0;
        uint32_t topicOffset;
        uint32_t payloadOffset;

        struct publishMsgHeader msgHead;

        char *pubBuff = NULL;
        struct msgQueue queueElem;

        topicOffset = sizeof(struct publishMsgHeader);
        payloadOffset = sizeof(struct publishMsgHeader) +
                        recvMetaData->topLen + 1;

        bufSizeReqd += sizeof(struct publishMsgHeader);
        bufSizeReqd += recvMetaData->topLen + 1;
        bufSizeReqd += dataLen + 1;
        pubBuff = (char *) malloc(bufSizeReqd);

        if(pubBuff == NULL)
        {
            APP_PRINT("malloc failed: recv_cb\n\r");
            return;
        }

        msgHead.topicLen = recvMetaData->topLen;
        msgHead.payLen = dataLen;
        msgHead.retain = recvMetaData->retain;
        msgHead.dup = recvMetaData->dup;
        msgHead.qos = recvMetaData->qos;
        memcpy((void*) pubBuff, &msgHead, sizeof(struct publishMsgHeader));

        /* copying the topic name into the buffer                        */
        memcpy((void*) (pubBuff + topicOffset),
               (const void*)recvMetaData->topic,
               recvMetaData->topLen);
        memset((void*) (pubBuff + topicOffset + recvMetaData->topLen),'\0',1);

        /* copying the payload into the buffer                           */
        memcpy((void*) (pubBuff + payloadOffset), (const void*) data, dataLen);
        memset((void*) (pubBuff + payloadOffset + dataLen), '\0', 1);

//        APP_PRINT("\n\rMsg Recvd. by client\n\r");
//        APP_PRINT("TOPIC: %s\n\r", pubBuff + topicOffset);
//        APP_PRINT("PAYLOAD: %s\n\r", pubBuff + payloadOffset);
//        APP_PRINT("QOS: %d\n\r", recvMetaData->qos);

        dev_data d = getJSONData(pubBuff + payloadOffset);
        printDevData(d);

        queueElem.m = convertStruct(d);

        if(recvMetaData->retain)
        {
            APP_PRINT("Retained\n\r");
        }

        if(recvMetaData->dup)
        {
            APP_PRINT("Duplicate\n\r");
        }

        /* filling the queue element details                              */
        queueElem.event = MSG_RECV_BY_CLIENT;
        queueElem.msgPtr = pubBuff;
        queueElem.topLen = recvMetaData->topLen;

        /* signal to the main task                                        */
        if(MQTT_SendMsgToQueue(&queueElem))
        {
            UART_PRINT("\n\n\rQueue is full\n\n\r");
        }
        break;
    }
    case MQTTClient_DISCONNECT_CB_EVENT:
    {
        gResetApplication = true;
        APP_PRINT("BRIDGE DISCONNECTION\n\r");
        break;
    }
    }
}

message_t convertStruct(dev_data input)
{
    message_t retVal;
    
    if(strcmp(input.type, "INIT") == 0)
    {
        retVal.type = INIT;
    }
    else if (strcmp(input.type, "DONE") == 0)
    {
        retVal.type = DONE;
    }
    else if (strcmp(input.type, "TIME") == 0)
    {
        retVal.type = TIME;
    }
    else if (strcmp(input.type, "PICK") == 0)
    {
        retVal.type = PICK;
    }
    else if (strcmp(input.type, "DROP") == 0)
    {
        retVal.type = DROP;
    }


    retVal.motor[0] = input.motor0;
    retVal.motor[1] = input.motor1;
    retVal.motor[2] = input.motor2;
    retVal.motor[3] = input.motor3;
    
    return retVal;
}

//*****************************************************************************
//
// Close the Doxygen group.
//! @}
//
//*****************************************************************************
