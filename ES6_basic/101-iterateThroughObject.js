/* eslint-disable */
export default function iterateThroughObject(reportWithIterator) {
    var employee = [];
    for (let employment of reportWithIterator) {
      employee.push(employment);
    }
    return employee.join(' | ');
  }