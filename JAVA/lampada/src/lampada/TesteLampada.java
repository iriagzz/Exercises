package lampada;


public class TesteLampada{

	public static void main(String[] args) {
	
		
		Lampada lampadaBranca = new Lampada(false,"philips", "branca", 12, 7.99);
		lampadaBranca.ascender();
		System.out.println(lampadaBranca);
		lampadaBranca.apagar();
		System.out.println(lampadaBranca);
	}

}
