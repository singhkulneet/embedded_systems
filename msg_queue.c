#include "msg_queue.h"

void motorQ_init()
{
    motorQ = xQueueCreate(QUEUE_LEN, sizeof(message_t));
}

void testQ_init()
{
    testQ = xQueueCreate(QUEUE_LEN, sizeof(message_t));
}

int txToTestQ(message_t m)
{
    BaseType_t xHigherPriorityTaskWoken = pdFALSE;
    BaseType_t result = xQueueSendToBackFromISR(testQ, &m, &xHigherPriorityTaskWoken);
    return  (pdPASS == result);
}

int txToMotorQ(message_t m)
{
    BaseType_t xHigherPriorityTaskWoken = pdFALSE;
    BaseType_t result = xQueueSendToBackFromISR(motorQ, &m, &xHigherPriorityTaskWoken);
    return  (pdPASS == result);
}

message_t rxFromTestQ()
{
    message_t m;
    xQueueReceive(testQ, &m, portMAX_DELAY);
    return m;
}

message_t rxFromMotorQ()
{
    message_t m;
    xQueueReceive(motorQ, &m, portMAX_DELAY);
    return m;
}
