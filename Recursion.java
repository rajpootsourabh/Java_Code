package com.programs;

public class Recursion {
    public static void main(String[] args) {
    System.out.println(add(5,10));
    }

    public static int add(int start, int end) {
       if(end > start){
           return start + add(start+1, end);
       }
       else{
           return end;
       }
    }
}
