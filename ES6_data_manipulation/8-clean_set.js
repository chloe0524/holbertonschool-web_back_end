export default (set, startString) => ((!startString || typeof startString !== 'string') ? '' : Array.from(set)
  .map((value) => (value.startsWith(startString) ? value.slice(startString.length) : ''))
  .filter((value) => value)
  .join('-'));
