export default class Model{
    constructor(){
        this.view = null;
        this.tasks = JSON.parse(localStorage.getItem('Tasks'));
        

        if(!this.tasks || this.tasks.length < 1 ){
            this.tasks = [{
                id: 0,
                title: 'Learn JS',
                description:'Watch JS tutorials',
                completed: false
            }];

            this.currentid = 1;
        } else {
            this.currentid = this.tasks[this.tasks.length - 1].id + 1;
        }
    }

    setView(view){
        this.view = view;
    }

    getTasks(){
        return this.tasks.map((todo) => ({...todo}));
    }

    addToDo(title,description){
        const todo = {
            id: this.currentid++,
            title,
            description,
            completed: false
        }

        this.tasks.push(todo);
        console.log(this.tasks);
        this.save();

        //Devolvemos un clon expandiendo el objeto
        return {...todo};

    }

    removeToDo(id){
        const index = this.findToDO(id);
        this.tasks.splice(index,1);
        this.save();
    }

    toggleCompleted(id){
        const index = this.findToDO(id);
        const todo = this.tasks[index];
        todo.completed = !todo.completed;
        this.save();
    }

    findToDO(id){
        return this.tasks.findIndex((todo) => todo.id === id);
    }

    save(){
        localStorage.setItem('Tasks',JSON.stringify(this.tasks));
    }

    editToDo(id,values){
        const index = this.findToDO(id);
        Object.assign(this.tasks[index],values);
        this.save();
    }
}