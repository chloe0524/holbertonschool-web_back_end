export default (map) => {
  if (!(map instanceof Map)) throw new Error('Cannot process');
  map.forEach((value, key) => (value === true ? map.set(key, 100) : null));
};
