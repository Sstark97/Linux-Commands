import Alert from './alert.js';

export default class AddToDo{
    constructor(){
        this.title = document.getElementById('title');
        this.description = document.getElementById('description');
        this.btn = document.getElementById('add');
        this.alert = new Alert('alert');
    }

    onClick(callBack){
        this.btn.onclick = () =>{
            if(title.value === '' || description.value === ''){
                this.alert.show('Title and descrìption are Required');
            } else{
                this.alert.hide();
                callBack(this.title.value,this.description.value);
            }
        }
    }
}