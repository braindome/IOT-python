age = 55
is_member = True 

if age >= 50:
  if is_member:
    print("Discount: 50%")
  else:
    print("Discount: 30%")
else:
  print("Regular price")

number = 2

match number:
  case 1:
    print("one")
  case 2 | 3:
    print("two or three")
  case _:
    print("other number")

# match-case / switch-case

match number:
    case 1:
        print('one')
    case 2 | 3:
        print('two or three')
    case _:
        print('other number')