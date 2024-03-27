--- FLUTTER ---
flutter create --empty --org it.limdev 
flutter create . // per ricreare il progetto
flutter channel stable 
flutter upgrade --force

macOS
	find ~/dev/projects/real_estate -type f -name 'Icon?' -print -delete;



Pod errors on Mac
	brew install ruby
brew upgrade ruby && brew link ruby --force
brew reinstall cocoapods
rm podfile.lock
sudo gem update --system 3.4.21


Packages
	flutter pub add http
	flutter clean
	flutter packages get
	flutter packages upgrade ( Optional - use if you want to upgrade packages )
	Restart Android Studio or Visual Studio

pub.dev
	flutter form builder // input widget aggiuntivi
	flutter form validator

linter:
  rules:
    use_key_in_widget_constructors: false
    prefer_const_constructors: false
    unnecessary_new: false
    prefer_const_literals_to_create_immutables: false
    prefer_interpolation_to_compose_strings: false
	
	
Widget sizing 
	Size size = MediaQuery.of(context).size;
	//largezza
	double width50 = size.width * 0.5;
	
	//altezza (contempla le barre superiori e inferiori)
	double screenHeight = size.height;
	
	double abovePadding = MediaQuery.of(context).padding.top;
	double appBarHeight = appBar.preferredSize.height;
	double leftHeight = screenHeight - abovePadding - appBarHeight;
	
	https://medium.flutterdevs.com/layoutbuilder-widget-in-flutter-d70d54b72a81
	
	

---- BEST PRACTICES ----
Code Style
	UpperCamelCase --> classi, enums, e typedefs
	lowerCamelCase --> istanze della classe, funzioni, variabili, e parametri
	snake_case --> nomi delle librerie, files	
	
Variable definition
	String name = 'Antonio';
	int age = 30;
	double points = 1232.73215;
	bool isAuthor = true;
	var emptyVal = ''; --> definizione implicita tramite type-check

Liste
	List<String> list = new List();
	var list = [];
	
	var articles = [];
	articles.add("Flutter");
	articles.add("Dart");
	print(articles);
	articles.remove("Dart");
	print(articles);	
	
Mappe (chiave : valore)	
	var info = new Map();
	var info = {};
	
	var identifier = { key1:value1, key2:value2 [,…..,key_n:value_n] }
	
	var info = new Map();
	info['name'] = 'Antonio';
	info['surname'] = 'Tedeschi';
	info['age'] = 30;
	
	
Costrutti Condizionali
	var age = 45;
	if (age < 30) {
	  print('young');
	} else if (age < 65) {
	  print('adult');
	} else {
	 print('elder');
	}
	
	
	var category = "adult";
	switch (category) {
	case "young":
	  {
		print("impetuous");
	  }
	  break;
	default:
	  {
		print("wise");
	  }
	  break;
	}
	

Cicli
	var collection = ['a', 'b', 'c'];
	for (var x in collection) {
		print(x);
	}

	collection.forEach((el) => print(el));
	
	
	var i = 0;
	while (i < 5) {
		print(i);
		i++;
	}
	
	
Funzioni
	int countArticles(List<String> articles) {
		return articles.length;
	  }

	countArticles(articles) {
		return articles.length;
	  }
	  
	//alternativa
	countArticles(articles) => articles.length;
	

Classi
	class Author {
	  String name;
	  String surname;
	  var articles = [];
	  

		Author(String name, String surname){
		this.name = name;
		this.surname = surname;
		}
	  
	  //alternativa
	  Author(this.name, this.surname);
	  
	@override
	String toString() => 'Author: $name $surname';
}
	  
	  
Metodi
	void startCooking (){}
	
	//metodo privato
	void _startTimer() {}
	
	
	//metodo statico: slegato dalla classe
	static bool compareWatts(Microwave a, Microwave b) {
		if (a.power > b.power) return -1;
		if (b.power > a.power) return 1;

		// else they're the same
		return 0;
	}
	
	print(Microwave.compareWatts(averageMicrowave, superMicrowave));

Modificatori
	static --> si applica a variabili e metodi rendendoli di classe (accessibili dall'esterno)
	final --> variabili che possono essere valorizzate solo una volta alla loro inizializzazione
	const --> per suggerire al compilatore che una variabile/widget è immutabile
	var --> permette di dichiarare una variabile il cui tipo sarà determinato dal suo primo utilizzo
	dynamic --> permette di dichiara una variabile dinamticamente tipizzata (un metodo può ritornare dynamic)

	

