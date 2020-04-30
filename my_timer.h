#ifndef MY_TIMER_H_
#define MY_TIMER_H_

/* C Library Header files */
#include <stddef.h>

/* Driver Header files */
#include <ti/drivers/Timer.h>

/* User Defined Headers */
#include "msg_queue.h"

/* Driver configuration */
#include "ti_drivers_config.h"

// Defining Timer Period
#define TIMER_PERIOD     6000

// Timer Function Prototypes
void timer_init();
void timerCallback(Timer_Handle myHandle);

#endif /* MY_TIMER_H_ */
