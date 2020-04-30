#ifndef MOTOR_TASK_H_
#define MOTOR_TASK_H_

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

// Including message queue header
#include "msg_queue.h"

/* Including User Defined Headers */
#include "ti_drivers_config.h"

// Main Task Function Prototype
void vMotorTask(void *pvParameters);

#endif /* MOTOR_TASK_H_ */
