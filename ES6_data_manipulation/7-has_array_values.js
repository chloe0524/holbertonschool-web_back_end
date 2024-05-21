export default (set, array) => array.reduce((exists, element) => exists && set.has(element), true);
