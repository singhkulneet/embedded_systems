#ifndef MESG_QUEUE_H_
#define MESG_QUEUE_H_

#include <FreeRTOS.h>
#include <queue.h>

#define QUEUE_LEN   120
#define ZERO        0

typedef enum dataType {INIT, DONE, TIME, PICK, DROP} data_t;

typedef struct messageStruct {
    data_t type;
    int motor[4];
} message_t;

QueueHandle_t testQ;
QueueHandle_t motorQ;

void motorQ_init();

void testQ_init();

int txToTestQ(message_t m);

int txToMotorQ(message_t m);

message_t rxFromTestQ();

message_t rxFromMotorQ();

#endif /* MESG_QUEUE_H_ */
