#include "test_task.h"

void vTestTask(void *pvParameters)
{
    // UART Variables
    UART_Params uartParams;

    /* Create a UART with data processing off. */
    UART_Params_init(&uartParams);
    uartParams.writeDataMode = UART_DATA_BINARY;
    uartParams.readDataMode = UART_DATA_BINARY;
    uartParams.readReturnMode = UART_RETURN_FULL;
    uartParams.readEcho = UART_ECHO_OFF;
    uartParams.baudRate = 115200;

    uart = UART_open(CONFIG_UART_0, &uartParams);

    if (uart == NULL) {
        /* UART_open() failed */
        while (1);
    }

    // Motor Control String Variables
    char        input;
    char        inputStr[15];
    const char  echoPrompt[] = "Starting Motor Controller Subsystem:\r\n";
    const char  motorNumPrompt[] = "Enter motor (0-3), s for script or t for test #: ";
    const char  motorScript[] = "\r\nEnter motor degrees '0,1,2,3': ";
    const char  motorDegree[] = "\r\nEnter desired angle (0-180): ";
    const char  movingMotor[] = "\r\nMoving Motor...\r\n";
    const char  movingMotors[] = "\r\nMoving all Motors...\r\n";
    const char  testCaseRun[] = "\r\nRunning test case ";
    const char  testCaseNum[] = "\r\nEnter test case # (1-10): ";

    int motorNum;
    int degrees;
    static int motorState[4] = {90, 90, 90, 90};
    int motorIn[4];
    int i;

    UART_write(uart, echoPrompt, sizeof(echoPrompt));
    message_t m;

    /* Main motor controller loop */
    while (1)
    {
        m = rxFromTestQ();
        strcpy(inputStr, "");
        dispCurent(motorState);
        UART_write(uart, motorNumPrompt, sizeof(motorNumPrompt));
        UART_read(uart, &input, 1);
        if(input == 's')
        {
            UART_write(uart, &input, 1);
            UART_write(uart, motorScript, sizeof(motorScript));
            UART_read(uart, &input, 1);
            while(input != '\r')
            {
                UART_write(uart, &input, 1);
                strncat(inputStr, &input, 1);
                UART_read(uart, &input, 1);
            }
            UART_write(uart, movingMotors, sizeof(movingMotors));
            char* token = strtok(inputStr, ",");
            for(i = 0; i < 4; i++)
            {
                sscanf(token, "%d", &motorIn[i]);
                motorState[i] = motorIn[i];
                token = strtok(NULL, ",");
            }

            m.type = DROP;
            for(i=0; i<4; i++)
            {
                m.motor[i] = motorState[i];
            }
            txToMotorQ(m);

            continue;
        }

        else if(input == 't')
        {
            UART_write(uart, &input, 1);
            UART_write(uart, testCaseNum, sizeof(testCaseNum));
            UART_read(uart, &input, 1);
            while(input != '\r')
            {
                strncat(inputStr, &input, 1);
                UART_write(uart, &input, 1);
                UART_read(uart, &input, 1);
            }
            sscanf(inputStr, "%d", &degrees);
            UART_write(uart, testCaseRun, sizeof(testCaseRun));

            dispTest(degrees);

            m.type = DROP;
            for(i=0; i<4; i++)
            {
                m.motor[i] = motorState[i];
            }
            txToMotorQ(m);

            continue;
        }

        sscanf(&input, "%d", &motorNum);
        UART_write(uart, &input, 1);
        UART_write(uart, motorDegree, sizeof(motorDegree));
        UART_read(uart, &input, 1);
        while(input != '\r')
        {
            strncat(inputStr, &input, 1);
            UART_write(uart, &input, 1);
            UART_read(uart, &input, 1);
        }
        sscanf(inputStr, "%d", &degrees);
        UART_write(uart, movingMotor, sizeof(movingMotor));
        motorState[motorNum] = degrees;

        m.type = PICK;
        for(i=0; i<4; i++)
        {
            m.motor[i] = motorState[i];
        }
        txToMotorQ(m);
    }
}

void dispCurent(int motorState[])
{
    char val[4];
    const char  motorVals[] = "Current Motor Values: ";
    UART_write(uart, motorVals , sizeof(motorVals));
    int i;
    for(i = 0; i < 3; i++)
    {
        snprintf(val, 4, "%d", motorState[i]);
        writeString(val);
        UART_write(uart, ",", 1);
    }
    snprintf(val, 4, "%d", motorState[3]);
    writeString(val);
    UART_write(uart, "\r\n", 2);
}

void dispTest(int num)
{
    char val[3];
    snprintf(val, 3, "%d", num);
    writeString(val);
    UART_write(uart, "...\r\n", 5);
}

void writeString(char str[])
{
    int i;
    for(i = 0; i < sizeof(str); i++)
    {
        if(str[i] == 0)
        {
            break;
        }
        UART_write(uart, &str[i], 1);
    }
}
