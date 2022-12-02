import serial

# Set a PORT Number & baud rate
PORT = 'COM3'
BaudRate = 9600

ARD= serial.Serial(PORT,BaudRate)


def Decode(int_sum):
    int_sum = int_sum.decode()
    int_sum = str(int_sum)
    if int_sum[0]=='Q':                       
        Ard1=str(int_sum[1:2])
        Ard2=str(int_sum[3:5])
        result= [Ard1, Ard2]
        return result
    
def Ardread(): # return list [Ard1,Ard2]
        if ARD.readable():
            LINE = ARD.readline()
            code=Decode(LINE) 
            return code
        else : 
            print("읽기 실패 from _Ardread_")



temp = Ardread()
# print(temp[0])
# print(float(temp[1]) * 0.01)
result = float(temp[0]) + (float(temp[1]) * 0.01)
print(result)