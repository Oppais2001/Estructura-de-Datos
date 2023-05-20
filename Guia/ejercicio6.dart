import 'dart:math';

void main(){
  Random random=Random();
  List<int> a= [4,3,2,2,1];
  List<int> b=[-3,2,8,0,1];
  List<int> c=[0,0,0,0,0];
  List<int> d=[];

  for(int i=0;i<5;i++){
    c[i]=a[i]*b[i];
  }
  print("lista resultado de la multiplicacion:");
  print(c);
  for(int j=0;j<5;j++){
    int aleatorio = -5 + random.nextInt(5);
    d.add(aleatorio);
  }
  c.addAll(d);
  print('Lista aleatoria:');
  print(d);
  print('Listas unidas:');
  print(c);
  c.sort();
  print('Lista ordenada:');
  List<int> e = c.reversed.toList();
  print(e);
}