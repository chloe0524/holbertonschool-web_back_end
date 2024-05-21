export default (map) => {
  if (!(map instanceof Map)) throw new Error('Cannot process');
  map.forEach((value, key) => (value === 1 ? map.set(key, 100) : null));
};
