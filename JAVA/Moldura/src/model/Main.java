package model;

import javax.swing.JOptionPane;

import view.Moldura;

public class Main {

	public static void main(String[] args) {
		float b1 = Float.parseFloat(JOptionPane.showInputDialog(null, "Insira o valor da base da moldura desejada: "));
		float h1 = Float.parseFloat(JOptionPane.showInputDialog(null, "Insira o valor da altura da moldura desejada: "));
		float e1 = Float.parseFloat(JOptionPane.showInputDialog(null, "Insira o valor da espessura da moldura desejada: "));
		
		Moldura m1 = new Moldura(b1, h1, e1);
		JOptionPane.showMessageDialog(null, "A área da moldura é: " + m1.calculaMoldura());
		float v1 = Float.parseFloat(JOptionPane.showInputDialog(null, "Insira o valor do cm2 (R$): "));
		JOptionPane.showMessageDialog(null, "O custo da moldura é: R$ " + m1.custoMoldura(v1));		

	}

}
