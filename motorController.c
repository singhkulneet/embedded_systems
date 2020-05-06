///*
// *  ======== motorController.c ========
// */
//
///* C Library Header files */
//#include <stdint.h>
//#include <stddef.h>
//#include <unistd.h>
//#include <stdio.h>
//#include <string.h>
//
///* Driver Header files */
//#include <ti/drivers/GPIO.h>
//#include <ti/drivers/UART.h>
//#include <ti/drivers/Timer.h>
//#include <ti/drivers/PWM.h>
//
///* User Defined Headers */
//#include "msg_queue.h"
//#include "motor_task.h"
//#include "test_task.h"
//#include "my_timer.h"
//#include "ti_drivers_config.h"
//
///* Priorities at which the tasks are created. */
//#define TEST_TASK_PRIORITY      ( tskIDLE_PRIORITY + 2 )
//#define MOTOR_TASK_PRIORITY     ( tskIDLE_PRIORITY + 1 )
//
///*
// *  ======== mainThread ========
// */
//void *mainThread(void *arg0)
//{
//    /* Call driver init functions */
//    PWM_init();
//    UART_init();
//    Timer_init();
//
//    /* Call user-defined init functions */
//    motorQ_init();
//    testQ_init();
//    timer_init();
//
//    message_t m;
//    m.type = INIT;
//
//    txToTestQ(m);
//
//    // Creating task threads
//    xTaskCreate(vTestTask,
//                "test_task",
//                1000,
//                NULL,
//                TEST_TASK_PRIORITY,
//                NULL);
//
//    xTaskCreate(vMotorTask,
//                "motor_task",
//                1000,
//                NULL,
//                MOTOR_TASK_PRIORITY,
//                NULL);
//
//    // Starting scheduler
//    vTaskStartScheduler();
//
//    for( ;; );
//}
