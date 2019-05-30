#include <stdio.h>



int main(void){


int i,j,infinito;
float mediaidade,mediaidademasc,mediaidadefem;
char avaliacao[10];

//CRIANDO VETORES COM AS INFORMAÇÕES DOS AVALIADOS (SEPARADOS EM MASCULINO E FEMININO)

char nomesfem[8][15] = {"Emanuela","Amora","Bianca","Vanessa","Leticia","Fernanda","Walesca","Adria",};
int idadefem[8] = {16,19,18,17,16,17,17,17};
char cursofem[8][20] = {"Telecomunicacoes-4","Eletrotecnica-6","Eletrotecnica-5","Eletrotecnica-5","Eletrotecnica-1","Telecomunicacoes-6","Telecomunicacoes-6","Telecomunicacoes-6"};
int avaliacaofem[8] = {1,2,1,3,2,2,1,1};
//------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
char nomesmasc[13][15] = {"Enzo","Guilherme","Caio","Victor","Eduardo","Edinaldo","João","Anderson","Italo","Mario","Fernando","Kayro","Werbster"};
int idadesmasc[13] = {17,18,17,18,17,17,17,19,16,18,20,17,16};
char cursomasc[13][20] = {"Eletrotecnica-4","Eletrotecnica-4","Telecomunicacoes-4","Mecanica-7","Edificacoes-5","Telecomunicacoes-5","Mecanica-7","Informatica-8","Eletrotecnica-6","Mecanica-7","Mecanica-6","Edificacoes-4","Informatica-2"};
int avaliacaomasc[13] = {3,1,2,1,2,1,2,2,3,2,1,1,3};

//LOOP INFINITO PARA O MENU FICAR SEMPRE RODANDO ATÉ QUE O USUARIO DIGITE 0
infinito = 1;
while(infinito>0){



printf("21 PESSOAS PARTICIPARAM DA PESQUISA\n");
printf("Entre eles 8 MULHERES e 13 HOMENS: \n\n");

printf("1 - Avaliacoes | 2 - Média de idade | 0 - SAIR\n");
printf("Escolha uma opção: ");
scanf("%d",&j);



//CONDIÇÃO DE PARADA DO PROGRAMA (USUARIO DIGITAR 0 OU NUMERO NEGATIVO)
if (j<=0){
	infinito = 0;
	
}


//PERCORRENDO OS VETORES MASCULINO E FEMININO (INDIVIDUALMENTE) PARA MOSTRAR OS DADOS

if(j ==1){

	for(i=0;i<=7;i++){
if(avaliacaofem[i] == 1){
	printf("Nome:%s | Idade:%d |  Curso: %s | Avaliacao: BOM| \n\n",nomesfem[i],idadefem[i],cursofem[i]);

}
if(avaliacaofem[i] == 2){
	printf("Nome:%s |  Idade:%d |  Curso: %s | Avaliacao: MEDIANA| \n\n",nomesfem[i],idadefem[i],cursofem[i]);

}
if(avaliacaofem[i] == 3){
	printf("Nome:%s |  Idade:%d |  Curso: %s | Avaliacao: RUIM| \n\n",nomesfem[i],idadefem[i],cursofem[i]);

}
if(avaliacaofem[i] == 4){
	printf("Nome:%s |  Idade:%d |  Curso: %s | Avaliacao: PESSIMO| \n\n",nomesfem[i],idadefem[i],cursofem[i]);

}
}


printf("------------------------------------------------------------------------------------------------------------\n\n");
for(i=0;i<=12;i++){
if(avaliacaofem[i] == 1){
	printf("Nome:%s | Idade:%d |  Curso: %s | Avaliacao: BOM| \n\n",nomesmasc[i],idadesmasc[i],cursomasc[i]);

}
if(avaliacaofem[i] == 2){
	printf("Nome:%s |  Idade:%d |  Curso: %s | Avaliacao: MEDIANA| \n\n",nomesmasc[i],idadesmasc[i],cursomasc[i]);

}
if(avaliacaofem[i] == 3){
	printf("Nome:%s |  Idade:%d |  Curso: %s | Avaliacao: RUIM| \n\n",nomesmasc[i],idadesmasc[i],cursomasc[i]);

}
if(avaliacaofem[i] == 4){
	printf("Nome:%s |  Idade:%d |  Curso: %s | Avaliacao: PESSIMO| \n\n",nomesmasc[i],idadesmasc[i],cursomasc[i]);



}
}
printf("-------------------------------------------------------------------------------------------------------------\n\n");
};


//CALCULANDO A MEDIA INVIDUAL DAS IDADES 

if (j==2){

printf("\n\n");
mediaidade = 0;
mediaidadefem =0;
mediaidademasc = 0;

for(i=0;i<=7;i++){
	mediaidadefem = mediaidadefem + idadefem[i];
	
	
}
printf("A media de idade entre as mulheres é de: %f\n",mediaidadefem/8);
//-------------------------------------------------------------------------

for (i=0;i<=12;i++){
		mediaidademasc = mediaidademasc + idadesmasc[i];
			
}
printf("A media de idade entre os homens é de: %f\n",mediaidademasc/13);

//CALCULANDO A MERDIA GERAL DAS IDADES

printf("A media geral das idades é: %f\n",(mediaidadefem + mediaidademasc)/21 );
printf("------------------------------------------------------------------------------------------------------------\n\n");
}
}

 return (0);
}