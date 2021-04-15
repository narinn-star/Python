#4-14(a)
log = '128.0.0.1 - - [12/Feb/2011:10:31:08 -0600] "GET /docs/test.txt HTTP/1.0"'
print(log)

#4-14(b)
address = log.split()[0]
print(address)

#4-14(c)
date = log[log.find('[') + 1:log.find(']')]
print(date)