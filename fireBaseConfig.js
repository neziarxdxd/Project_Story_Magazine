



		
		

var firebaseConfig = {
	    apiKey: "AIzaSyB3iOA424jKYZAgMfPDM3qXc6Z2isbg_Qs",
	    authDomain: "myfirstapp-5390e.firebaseapp.com",
	    databaseURL: "https://myfirstapp-5390e.firebaseio.com",
	    projectId: "myfirstapp-5390e",
	    storageBucket: "",
	    messagingSenderId: "899197736247",
	    appId: "1:899197736247:web:eb20d1284ca521d5"
};

	  

	  // Initialize Firebase
firebase.initializeApp(firebaseConfig);
	  function clickMe(){
	  	var id = document.getElementById("mainID").value;
	  	var name = document.getElementById("mainText").value;		
		var today = new Date();
		var date = today.getFullYear()+'-'+(today.getMonth()+1)+'-'+today.getDate();
		var time = today.getHours() + ":" + today.getMinutes() + ":" + today.getSeconds();
		
		
		
	  	var firebaseRef= firebase.database().ref();
	  	var x = {name: name, date:date, time: time}
	  	firebaseRef.child(id).set(x);	  
}

