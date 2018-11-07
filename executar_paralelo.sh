#!/bin/bash
DIR=`pwd`
PATH=tempos_paralelo
cd $DIR/src/java

echo "Compilando código-fonte"
javac *.java

echo "Movendo código-fonte compilado"
mv *.class $DIR/$PATH/
cd $DIR/$PATH/

echo "Realizando execução paralelo"
for i in {0..9};
do
	echo "Execução " $((i+1))
	#java MultiThread > tempo_paralelo_$i
done

echo "Deletando arquivos compilados"
rm *.class
cd $DIR

echo "Finalizado: tempos de execução paralelo"