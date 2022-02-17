def fizz_buzz(input_number):
    if input_number % 15 == 0:
      print("FizzBuzz")
    elif input_number % 3 == 0:
      print("Fizz")
    elif input_number % 5 == 0:
      print("Buzz")
    else:
      print(str(input_number))

print("数字を入力してください")
  
input_number = int(input())

print("結果は...")
fizz_buzz(input_number)