################################################################################
# Automatically-generated file. Do not edit!
################################################################################

# Add inputs and outputs from these tool invocations to the build variables 
C_SRCS += \
../src/Configuration/BuildVersion.c 

OBJS += \
./src/Configuration/BuildVersion.o 

C_DEPS += \
./src/Configuration/BuildVersion.d 


# Each subdirectory must supply rules for building sources it contributes
src/Configuration/%.o: ../src/Configuration/%.c
	@echo 'Building file: $<'
	@echo 'Invoking: Cross GCC Compiler'
	gcc -I"C:\Workspaces\Sample\src" -O3 -Wall -c -fmessage-length=0 -MMD -MP -MF"$(@:%.o=%.d)" -MT"$(@)" -o "$@" "$<"
	@echo 'Finished building: $<'
	@echo ' '


