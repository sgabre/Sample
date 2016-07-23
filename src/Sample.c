/*
 ============================================================================
 Name        : Sample.c
 Author      : GSI
 Version     :
 Copyright   : Your copyright notice
 Description : Hello World in C, Ansi-style
 ============================================================================
 */

#include <stdio.h>
#include <stdlib.h>

#include "ProductVersion.h"
#include "./Configuration/BuildVersion.h"

int main(void)
{
	printf("--Software--\n");
	printf("Name: %s\n", SystemSoftwareName);
	printf("Reference: %s\n", SystemSoftwareReference);
	printf("Version: V%s\n", SystemSoftwareVersion);
	printf("--Hardware--\n");
	printf("Version: UID-%s\n", SystemHardwareVersion);
	printf("--Configuration Manager--\n");
	printf("Build Date: %s\n", BuildDate);
	printf("Build Long Version: %s\n", BuildLongVersion);
	printf("Build Short Version: %s\n", BuildShortVersion);
	return 0;
}
