#ifndef TEST_TASK_H_
#define TEST_TASK_H_

#include <stdint.h>
#include <stddef.h>
#include <unistd.h>
#include <stdio.h>
#include <string.h>

/* Driver Header files */
#include <ti/drivers/GPIO.h>
#include <ti/drivers/UART.h>
#include <ti/drivers/Timer.h>
#include <ti/drivers/PWM.h>

/* Driver configuration */
#include "ti_drivers_config.h"

//including message queue header file
#include "msg_queue.h"

// Global UART
UART_Handle uart;

// User-Defined Helper Functions
void dispCurent(int motorState[]);
void dispTest(int num);
void writeString(char str[]);

// Main Task Function Prototype
void vTestTask(void *pvParameters);

#endif /* TEST_TASK_H_ */
