import PyObject = require('./PyObject');
import enums = require('./enums');

class PyLong extends PyObject{
  private n: number;
  constructor(n: number){
    super(enums.PyType.TYPE_LONG);
    this.n = n;
  }
  getLong(): number{
    return this.n;
  }
}

export = PyLong;
