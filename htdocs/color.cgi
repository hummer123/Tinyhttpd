#!/usr/bin/perl -Tw

use strict;		#为了帮助我们寻找错误拼写造成的错误
use CGI;        #通过use关键字引入CGI模块

my($cgi) = new CGI; #创建一个新的CGI对象

print $cgi->header; #输出CGI的标准头部信息
my($color) = "blue"; #创建变量color 并默认设置为blue
#判断输入的参数中是否有color，如果有则将其对应的值赋给color
$color = $cgi->param('color') if defined $cgi->param('color');

#title为大写的 color对应的值的字符串, 背景设置成color的值
print $cgi->start_html(-title => uc($color),
                       -BGCOLOR => $color);
print $cgi->h1("This is $color");  #html标题为 This is 颜色
print $cgi->end_html; #结束html文件
