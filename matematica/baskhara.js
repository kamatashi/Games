const [a,b,c] = [3,5,1]

const baskhara = (a, b, c) => {
  const delta = Math.sqrt(b**2 -4*a*c)
  const x1 = (-b + delta) / 2*a
  const x2 = (-b - delta) / 2*a

  return [x1, x2]
}

const raizes = baskhara(a,b,c)

console.log(raizes)
