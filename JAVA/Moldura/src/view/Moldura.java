package view;

public class Moldura {

	//Atributos
	public float base;
	public float altura;
	public float espessura;

	//Construtores

	public Moldura(float b, float h, float e) {
		this.base = b;
		this.altura = h;
		this.espessura = e;
	}

	//Metodo
	
	public float calculaMoldura() {
		float resultado = (this.base * this.altura) - ((this.base-(2*this.espessura))*(this.altura-(2*this.espessura)));
		return resultado;
		
	}
	
	public float custoMoldura(float valor) {
		float custo = this.calculaMoldura()  * valor;
		return custo;
		
	}



}




