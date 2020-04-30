#include "my_timer.h"

void timer_init()
{
    Timer_Handle timer0;
    Timer_Params params;

    Timer_Params_init(&params);
    params.period = TIMER_PERIOD;
    params.periodUnits = Timer_PERIOD_US;
    params.timerMode = Timer_CONTINUOUS_CALLBACK;
    params.timerCallback = timerCallback;

    timer0 = Timer_open(Board_TIMER0, &params);

    if (timer0 == NULL) {
        /* Failed to initialized timer */
        while (1) {}
    }

    if (Timer_start(timer0) == Timer_STATUS_ERROR) {
        /* Failed to start timer */
        while (1) {}
    }
}

void timerCallback(Timer_Handle myHandle)
{
    message_t message;
    message.type = TIME;
    txToMotorQ(message);
}
