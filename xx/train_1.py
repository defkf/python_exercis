#!/usr/bin/python
#-*- coding=utf-8 -*-

import urllib,urllib2,os,re,sys

#1.
# def pattern(n):
# 	return '\n'.join(str(i) * i for i in xrange(1, n + 1))

# print pattern(3)

#2.
# def largest(n ,xs):

# 	return sorted(xs)[-n:]

# print largest(2,[10,9,8,7,6,5,4,3,2,1])
# print largest(3,[5,1,5,2,3,1,2,3,5])
# print largest(7,[9,1,50,22,3,13,2,63,5])

#3.
# def candies(s):
# 	if len(s) <= 1:
# 		return -1
# 	else:
# 		lis = []
# 		for i in s:
# 			lis.append(max(s) - i)
# 		return sum(lis)

# print candies([5,8,6,4])
# print candies([1,2,4,6])
# print candies([1,2])
# print candies([4,2])


# 4.
# def x(n):
# 	return '\n'.join(''.join(str(j) for j in xrange(i + 1, n + 1)) for i in xrange(n))
# print x(5)

#5.1三角形
# def x(n):
# 	for i in range(n):
# 		print ' ' * (n-1-i) + '*' * (i+(i-1))
# x(10)

#5.2
# def x(n):
# 	for i in range(n):
# 		print ' ' * (n-1-i) + str(''.join(str(j) for j in xrange(1, n + 1)))
# x(10)
#5.3
# def x(n):
# 	if n > 10:
# 		x = n%10
# 		y = n/10
# 		return ''.join((''.join(str(i) for i in xrange(1,11)) * y) + (''.join(str(i) for i in xrange(1,x+1))))
# 	else:
# 		return ''.join(str(i) for i in xrange(1,n+1))

# print x(6)


#5.2最终版
# def pattern(n):
    # if n <= 0:
    #     return ''
    
    # sb = ''
    # number_string = '1234567890'
    
    # repetition = number_string * (n/10) + number_string[:n % 10]
    # for x in range(n,0,-1):
    #     sb += ' ' * (x-1) + repetition + ' '*(n-x) + '\n'
    # return sb[:-1]


#6.
# def high_and_low(number):
# 	ll = []
# 	for i in number.split(' '):
# 		ll.append(int(i))
# 	return '%s  %s' %(max(ll),min(ll)) 
# print high_and_low("4 5 29 54 4 0 -214 542 -64 1 -3 6 -6")

#7.
# def filter_list(n):
# 	lis = []
# 	for i in n:
# 		if type(i) == type(1):
# 			lis.append(i)
# 		else:
# 			pass
# 	return lis

# filter_list([1,2,'a','b']) 
# filter_list([1,'a','b',0,15])


# t = [1,2,3,4]
# t_copy = copy_list(t)
# t[1] += 5
# t == [1,7,3,4]
# t_copy = [1,2,3,4]

#8.
# def copy_list(l):
# 	n = list(l)
# 	return n

# t = [1,2,3,4]
# t_copy = copy_list(t)
# t[1] += 5
# print t
# print t_copy

#9.
# def d(n,x,y):
# 	if n % x == 0 and n % y == 0:
# 		print 'true because %s is divisible by %s and %s' %(n,x,y)
# 	elif n % x != 0 and n % y != 0:
# 		print 'false because %s is neither divisible by %s nor %s' %(n,x,y)
# 	elif n % x != 0:
# 		print 'false because %s is not divisible by %s' %(n,x)
# 	else:
# 		print 'false because %s is not divisible by %s' %(n,x)
# d(100,3,5)

# 10测试.
# def d(n,x,y):
# 	a = True
# 	b = False
# 	if n % x == 0 and n % y == 0:
# 		return a
# 	else:
# 		return b
# print d(100,3,5)

#11.
# def min_max(lst):
# 	l = []
# 	l.append(max(lst))
# 	l.append(min(lst))
# 	return sorted(l) 

# print min_max([1])

#12.
# def sort_dict(d):
#   'return a sorted list of tuples from the dictionary'
#   s = []
#   for i in d:
#       s.append((i,d[i]))
#   b = sorted(s,key=lambda s_tuple:s_tuple[1],reverse=1)
#   return b

# print sort_dict({1:5,3:10,2:2,6:3,8:8})
x = '<script>'
print  urllib.unquote(x)
