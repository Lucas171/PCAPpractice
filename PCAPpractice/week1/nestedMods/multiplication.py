from addition import addition

def multiply(num1, num2):
  return num1 * num2

if __name__ == '__main__':
  added_num = addition(5, 5) # 10
  answer = multiply(added_num, 10) # 100
  print(answer)