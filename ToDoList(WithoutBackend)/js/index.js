import Model from './model.js';
import View from './view.js';

document.addEventListener('DOMContentLoaded', function(){
    const model = new Model();
    const view = new View();

    model.setView(view);
    view.setModel(model);

    view.render();

});