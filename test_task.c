#include "test_task.h"

void * vTestTask(void *pvParameters)
{
    message_t m;

    /* Main motor controller loop */
    while (1)
    {
        m = rxFromTestQ();

        txToMotorQ(m);
    }
}
