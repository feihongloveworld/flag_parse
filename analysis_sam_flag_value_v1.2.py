# -*- coding: UTF-8 -*-
import os,sys

def Dec2Bin(dec):
	'transform Dec to Bin'
    	result = ''
	
    	if dec:
        	result = Dec2Bin(dec // 2)
        	return result + str(dec % 2)
    	else:
        	return result

def Pos_Int(_str):
	if '-' in _str or '.' in _str:
		raise Exception("the sam flag value must be greater than 0 and a int")
	elif _str.isdigit():
		return str(_str)
	else:
		raise Exception("the str could not transform to int !!")


def Completion_Bin(_Bin_Str):
	length = len(_Bin_Str)
	if length > 12:
		raise Exception("the flag bits must be lower than 13")
	elif length == 12:
		return _Bin_Str
	else:
		return '0'*(12-length) + _Bin_Str
		
def my_print(_in,_bit,_info):
	if _in[_bit-1] == '1':
		print _info
	else:
		pass

def flag2value_dic():
        flag2value  =  {1:'pair end reads',
			2:'each reads properly mapped',
			3:'this read unmapped',
			4:'mate read unmapped',
                        5:'this read being reverse complemented',
			6:'mate read being reverse complemented',
                        7:'this read is read_1',
			8:'this read is read_2',
			9:'the record is secondary alignment',
                        10:'this read is not passing filters',
			11:'this read is PCR or optical duplicate',
			12:'the record is supplementary alignment'}
	return flag2value

def Analysis_Flag(_flag_bit_str):
	_string = _flag_bit_str[::-1]
	flag2value = flag2value_dic()
	for i in range(0,13):
		my_print(_string,i,flag2value[i])
		

def information_print(_str,_bit_str,_bit):
        print '='*10 + ' sam flag value analysis information ' + '='*10 + '\n'
        print 'the record flag value is %s'%_str
        print 'the record flag bit value is %s'%_bit
        print '\n' + '='*20 + '\n'
	Analysis_Flag(_bit_str)
	print "\nthat's all ^_^ !! "
	print '='*30

	
if __name__ == '__main__':
	if len(sys.argv) == 1:
		print 'python ~/fh_scripts/analysis_sam_flag_value.py flagvalue'
	else:
		input_str = sys.argv[1]
		input_str = Pos_Int(input_str)
		input_int = int(input_str)
		input_bit = Dec2Bin(input_int)
		input_bit_str = Completion_Bin(str(input_bit))
		information_print(input_str,input_bit_str,input_bit)




## feihong@Geneseeq in 2019.1.8
