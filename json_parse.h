#ifndef JASON_PARSE_H
#define JASON_PARSE_H

#include "cJSON.h"
#include "uart_term.h"


typedef struct dev_dataStruct {
    char* type;  
    int motor0;
    int motor1;
    int motor2;
    int motor3;
} dev_data;

/* Prints out struct values to UART */
void printDevData(dev_data d);

/* Wrapper for cJSON_GetObjectItemCaseSensitive function*/
int getIntValue(cJSON *obj, char *field);

char *getStrValue(cJSON *obj, char *field);

/* Returns a struct with values from str string (JSON format) */
dev_data getJSONData(char *str);

#endif /* JASON_PARSE_H */
