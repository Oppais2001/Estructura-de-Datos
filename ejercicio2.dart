import 'dart:io';
import 'dart:math';
void main(){
  List<int>lista1 = [14,2,5,3,9];
  List<int>lista2=[];
  List<int>lista3=[];
  List<int>lista4=[]
  for(int i=0; i<5 ;i++){
    print("ingrese valores a la lista:");
    int x = int.parse(stdin.readLineSync()!);
    lista2.add(x);
  }
  for(int i=0;i<5;i++){
    int x=Random(-15,-25);
  }
  for(int i=0;i<5;i++){
    lista3[i]=lista1[i]-lista2[i];
  }
  print(lista2);
  print(lista3);
}