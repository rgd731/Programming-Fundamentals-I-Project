questions = {
  "easy": {
    "What is the correct syntax to print 'Hello World'?\n\n(a) print('Hello World')\n(b) p('Hello World')\n(c) print 'Hello World'\n(d) console.log('Hello World');\n":
    ["a", "a.", "print('hello world')", "print(\"hello world\")"],
    "Which of the following is the correct way to create a comment in Python?\n(a) //Comment\n(b) 'Comment'\n(c) #Comment\n(d) *Comment*\n":
    ["c", "c.", "#comment"],
    "Which arithmetic operator is used to find the\nremainder when dividing two numbers?\n\n(a) *\n(b) //\n(c) **\n(d) %\n":
    ["d", "d.", "%"],
    "What index represents the number '34' in the following list?\n[45, 64 , 77, 34]\n\n(a) 1\n(b) 2\n(c) 3\n(d) 4\n":
    ["c", "c.", "3", "three"],
    "What is the output of the following code?\nx = 3\ny = 3\nprint(x**y)\n\n(a) 15\n(b) 27\n(c) 9\n(d) 33\n":
    ["b", "b.", "27", "twenty-seven", "twentyseven", "twenty seven"]
  },
  "medium": {
    "Which data type is unordered, mutable, and does not allow duplicate values?\n\n(a) Dictionary\n(b) Set\n(c) List\n(d) Tuple\n":
    ["b", "b.", "set", "a set", "sets"],
    "What is the output in the following code?\n\nx=5\ndef my_func():\n  if x>2:\n    x=x+3\n  else:\n    x=x+5\nmy_func()\nprint(x)\n\n(a) 5\n(b) 3\n(c) 10\n(d) 8\n":
    ["a", "a.", "5", "five"],
    "What is the length of the dictionary?\nmy_students = {'Jonathan':'84',\n'Stephanie': {'Final':'95', 'Midterm':88}}\n\n(a) 2\n(b) 5\n(c) 4\n(d) 1\n":
    ["a", "a.", "2", "two"],
    "What is the value of my_list?\n\nmy_list = ['Hello World']\nmy_list = my_list.split()\n\n(a) ['Hello','World']\n(b) ['Coding','is','Awesome]\n(c) 'Hello World'\n(d) Error\n":
    ['a', 'a.', "['Hello','World']"],
    "Which of the following code will print the\neven numbers only in the following code?\nmy_list = [0,1,2,3,4,5,6,7,8,9]\nXXX\n  print(my_list[i])\n\n(a) for i in my_list\n(b) for i in range(len(my_list))\n(c) for i in range(1,len(my_list))\n(d) for i in range(0,len(my_list),2)":
    ["d", "d.", "for i in range(0,len(my_list),2)"]
  },
  "hard": {
    "What code will create a custom exception type?\n\n(a) class CustomError(Exception):\n(b) def CustomError(Exception):\n(c) class CustomError(exception):\n(d) def CustomError(Exception)\n":
    ["a", "a.", "class CustomError(Exception)"],
    "What is the output of the following code?\n\nx=int(5.4)\ny=int(5.5)\nz=int(5.6)\nprint(x,y,z)\n\n(a) 6 6 6\n(b) 5 6 6\n(c) 5 5 6\n(d) 5 5 5\n":
    ["d", "d.", "555", "5 5 5"],
    "What is the output of the following code?\n\nmy_str1 = ['hello']\nmy_str2 ='world!'\nmy_str1.extend(y)\nprint(my_str1)\n\n(a) ['hello', 'world!']\n(b) Error\n(c) ['hello','w','o','r','l','d','!']\n(d) ['hello world!']\n":
    ["c", "c.", "['hello','w','o','r','l','d','!']"],
    "What is the output using this slice notation?\n\nmy_str = '123456789'\nprint(my_str[:2:-1])\n\n(a) 21\n(b) 987654\n(c) 456789\n(d) 21987654\n":
    ["b", "b.", "987654"],
    "What is the value of my_list?\n\nmy_list = ['Coding is Awesome!']\nmy_list = my_list.split()\nmy_list = my_list.split('!')\n\n(a) ['Coding','is','Awesome!']\n(b) ['Coding','is','Awesome','']\n(c) Error\n(d) ['Coding','is','Awesome','!']\n":
    ['c', 'c.', 'error']
  }
}
