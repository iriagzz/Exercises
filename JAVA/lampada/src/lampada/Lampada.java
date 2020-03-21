package lampada;

public class Lampada {
	
	//atributos
	private boolean estado; //false: desligado    true: ligado
	private String marca;
	private String cor;
	private int voltagem;
	private double preco;

	//construtores
	public Lampada(boolean es, String m, String c, int v, double p) {
		this.estado = es;
		this.marca = m;
		this.cor = c;
		this.voltagem = v;
		this.preco = p;		
	}
	//metodos getters
	public boolean isEstado(){ //pode ser get ou is
		return this.estado;
	}
	public String getMarca(){
		return this.marca;
	}
	public String getCor(){
		return this.cor;
	}
	public int getVoltagem(){
		return this.voltagem;
	}
	public double getPreco(){
		return this.preco;
	}

	//metodos setters
	public void setEstado(boolean est){
		this.estado = est;
	}
	public void setMarca(String marca){
		this.marca = marca;
	}
	public void setCor(String cor){
		this.cor = cor;		
	}
	public void setVoltagem(int voltagem){
		this.voltagem = voltagem;
	}
	public void setPreco(double preco){
		this.preco = preco;
	}

	//metodos

	//toString

	public String toString() {
		String retorno = "";

		retorno += "Lampada:\n";
		retorno += "\tMarca: " + this.marca;
		retorno += "\tCor: " + this.cor;
		retorno += "\tVoltagem: " + this.voltagem;
		retorno += "\tPreco: " + this.preco;
		retorno += "\tEstado: " + estaLigada();

		return retorno;
	}


	public String estaLigada(){
		if(this.estado == true) { 
			return "Está ligada.";
		}if(this.estado == false) {
			return "Está desligada.";
		}else{
			return "Está meia-luz.";
		}
	}

	//Metodo ascender
	public void ascender(){
		setEstado(true);
	}

	//Metodo apagar
	public void apagar(){
		setEstado(false);
	}


}


