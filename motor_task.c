#include "motor_task.h"

// Keeping track of motor states
static int motorCurNum[4] = {90, 90, 90, 90};
static int goal_state[4];

// Global PWMs
PWM_Handle pwm1 = NULL; // g
PWM_Handle pwm2 = NULL; // z
PWM_Handle pwm3 = NULL; // y
PWM_Handle pwm4 = NULL; // x

int moveMotor(int motor_num);
int convert(int degrees, int motor_num);

void vMotorTask(void *pvParameters)
{
    /* Period and duty in microseconds */
    uint32_t   pwmPeriod = 20000;

    PWM_Params paramsPWM;

    PWM_Params_init(&paramsPWM);
    paramsPWM.dutyUnits = PWM_DUTY_US;
    paramsPWM.periodUnits = PWM_PERIOD_US;
    paramsPWM.periodValue = pwmPeriod;

    paramsPWM.dutyValue = convert(90, 0);
    pwm1 = PWM_open(CONFIG_PWM_0, &paramsPWM);
    if (pwm1 == NULL) {
        /* CONFIG_PWM_0 did not open */
        while (1);
    }
    PWM_start(pwm1);

    paramsPWM.dutyValue = convert(90, 1);
    pwm2 = PWM_open(CONFIG_PWM_1, &paramsPWM);
    if (pwm2 == NULL) {
        /* CONFIG_PWM_1 did not open */
        while (1);
    }
    PWM_start(pwm2);

    paramsPWM.dutyValue = convert(90, 2);
    pwm3 = PWM_open(CONFIG_PWM_2, &paramsPWM);
    if (pwm3 == NULL) {
        /* CONFIG_PWM_2 did not open */
        while (1);
    }
    PWM_start(pwm3);

    paramsPWM.dutyValue = convert(90, 3);
    pwm4 = PWM_open(CONFIG_PWM_3, &paramsPWM);
    if (pwm4 == NULL) {
        /* CONFIG_PWM_3 did not open */
        while (1);
    }
    PWM_start(pwm4);

    static message_t m;

    typedef enum {IDLE, DONE_M, MOVING_0, MOVING_1, MOVING_2, MOVING_3} motorState_t;
    typedef enum {NONE, PICKING, DROPPING} motorDir_t;

    static motorState_t motorState = IDLE;
    static motorDir_t motorDir = NONE;

    int ret;
    int i;

    while(1)
    {
        m = rxFromMotorQ();
        switch(motorState)
        {
            case IDLE:
                if(m.type == DROP)
                {
                   motorState = MOVING_0;
                   motorDir = DROPPING;
                   for(i=0; i<4; i++)
                   {
                       goal_state[i] = m.motor[i];
                   }
                   moveMotor(0);
                }
                else if(m.type == PICK)
                {
                   motorState = MOVING_3;
                   motorDir = PICKING;
                   for(i=0; i<4; i++)
                   {
                       goal_state[i] = m.motor[i];
                   }
                   moveMotor(3);
                }
            break;
            case MOVING_0:
                if(m.type == TIME)
                {
                  ret = moveMotor(0);

                  if(ret)
                  {
                      if(motorDir == DROPPING) {
                          motorState = MOVING_1;
                      }
                      else {
                          motorState = DONE_M;
                      }
                  }
                }
            break;
            case MOVING_1:
            if(m.type == TIME)
            {
                ret = moveMotor(1);

                if(ret)
                {
                    if(motorDir == DROPPING) {
                        motorState = MOVING_2;
                    }
                    else {
                        motorState = MOVING_0;
                    }
                }
            }
            break;
            case MOVING_2:
                if(m.type == TIME)
                {
                  ret = moveMotor(2);

                  if(ret)
                  {
                      if(motorDir == DROPPING) {
                          motorState = MOVING_3;
                      }
                      else {
                          motorState = MOVING_1;
                      }
                  }
                }
            break;
            case MOVING_3:
                if(m.type == TIME)
                {
                    ret = moveMotor(3);

                    if(ret)
                    {
                        if(motorDir == DROPPING) {
                            motorState = DONE_M;
                        }
                        else {
                            motorState = MOVING_2;
                        }
                    }
                }
            break;
            case DONE_M:
                m.type = DONE;
                txToTestQ(m);
                motorState = IDLE;
            break;
        }
    }
}

int moveMotor(int motor_num)
{
    int cur_state;
    cur_state = motorCurNum[motor_num];

    if(cur_state < goal_state[motor_num])
    {
        switch(motor_num)
        {
            case 0: PWM_setDuty(pwm1, convert(cur_state, motor_num));
                break;
            case 1: PWM_setDuty(pwm2, convert(cur_state, motor_num));
                break;
            case 2: PWM_setDuty(pwm3, convert(cur_state, motor_num));
                break;
            case 3: PWM_setDuty(pwm4, convert(cur_state, motor_num));
                break;
//            case 0: PWM_setDuty(pwm1, cur_state);
//                break;
//            case 1: PWM_setDuty(pwm2, cur_state);
//                break;
//            case 2: PWM_setDuty(pwm3, cur_state);
//                break;
//            case 3: PWM_setDuty(pwm4, cur_state);
//                break;
        }

        motorCurNum[motor_num] = cur_state + 1;
    }
    else
    {
        switch(motor_num)
        {
            case 0: PWM_setDuty(pwm1, convert(cur_state, motor_num));
                break;
            case 1: PWM_setDuty(pwm2, convert(cur_state, motor_num));
                break;
            case 2: PWM_setDuty(pwm3, convert(cur_state, motor_num));
                break;
            case 3: PWM_setDuty(pwm4, convert(cur_state, motor_num));
                break;
//            case 0: PWM_setDuty(pwm1, cur_state);
//                break;
//            case 1: PWM_setDuty(pwm2, cur_state);
//                break;
//            case 2: PWM_setDuty(pwm3, cur_state);
//                break;
//            case 3: PWM_setDuty(pwm4, cur_state);
//                break;
        }

        motorCurNum[motor_num] = cur_state - 1;
    }


    // Checking if goal state is achieve
    if(cur_state == goal_state[motor_num])
    {
        return 1;
    }
    else
    {
        return 0;
    }
}

int convert(int degrees, int motor_num)
{
    int ret_val = 1000;
    switch(motor_num)
    {
        case 0: ret_val = 870 + (6 * degrees);
            break;
        case 1: ret_val = 700 + (8 * degrees);
            break;
        case 2: ret_val = 1250 + (6 * degrees);
            break;
        case 3: ret_val = 800 + (8 * degrees);
            break;
    }
    return ret_val;
}

