# quoridor.py
A python version of strategy board game "Quoridor", with AI and a graphic interface.

![](https://raw.githubusercontent.com/alainrinder/quoridor.py/master/img/Picture.600x300.jpg)

### How to play
With this script, you can:
* Play against someone else (Human vs Human)
* Play against a bot (Human vs AI)
* Make one bot to play against another (AI vs AI)

For a quick play against IA, execute "python main.py --players=Me:Human,IA:BuildAndRunBot". 
Otherwise, execute "python main.py -h" to display usage.

For human players :
* Press "p" to move your pawn: it will display the possible moves, so you can click where you want your pawn to go;
* Press "f" to place a fence: if you still have remaining fences, it will display every possible position:
  * If you click between 2 squares vertically aligned, it will place an horizontal fence between them, starting from left at this square;
  * if you click between 2 squares horizontally aligned, it will place a vertical fence between them, starting from top at this square.


### Screenshot
![Screenshot](https://raw.githubusercontent.com/alainrinder/quoridor.py/master/img/Screenshot.png)

### Contributors
* Alain Rinder ([GitHub](https://github.com/alainrinder))
* Pierre Rinder ([GitHub](https://github.com/prinder))
