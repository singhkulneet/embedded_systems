#include "json_parse.h"
#include <string.h>


/* Prints out struct values to UART */
void printDevData(dev_data d) {

    UART_PRINT("Recived Struct {\r\n\r\n");
    UART_PRINT("    type: %s\r\n", d.type);
    UART_PRINT("    motor0: %d\r\n", d.motor0);
    UART_PRINT("    motor1: %d\r\n", d.motor1);
    UART_PRINT("    motor2: %d\r\n", d.motor2);
    UART_PRINT("    motor3: %d\r\n", d.motor3);
    UART_PRINT("\r\n}\r\n");
}


/* Wrapper for cJSON_GetObjectItemCaseSensitive function*/
int getIntValue(cJSON *obj, char *field) {

    cJSON *val_obj = cJSON_GetObjectItemCaseSensitive(obj, field);
    return (val_obj != NULL) ? val_obj->valueint : -1;       // -1 indicates value not found
}

char *getStrValue(cJSON *obj, char *field) {

    cJSON *val_obj = cJSON_GetObjectItemCaseSensitive(obj, field);
    return (val_obj != NULL) ? val_obj->valuestring : "None";
}


/* Returns a struct with values from str string (JSON format) */
dev_data getJSONData(char *str) {

    // initialize struct
    dev_data d_data = {"None", -1, -1, -1, -1};

    cJSON *json_obj = cJSON_Parse(str);

    int size = cJSON_GetArraySize(json_obj);
    if(size == 0) {
        UART_PRINT("ERROR: Empty string or improper format.\r\n");
        return d_data;
    }

    d_data.type = getStrValue(json_obj, "type");
    d_data.motor0 = getIntValue(json_obj, "motor0");
    d_data.motor1 = getIntValue(json_obj, "motor1");
    d_data.motor2 = getIntValue(json_obj, "motor2");
    d_data.motor3 = getIntValue(json_obj, "motor3");

    cJSON_Delete(json_obj);
    return d_data;
}
