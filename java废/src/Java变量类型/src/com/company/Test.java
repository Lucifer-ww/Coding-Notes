package com.company;

public class Test {
    public void setAge()
    {
        int age = 0;
        age = age + 7;
        System.out.println("age is:" + age);
    }
    public static void main(String[] args) {
	// write your code here
        System.out.println("hello world");
        int a;
        Test test = new Test();
        test.setAge();
    }
}
