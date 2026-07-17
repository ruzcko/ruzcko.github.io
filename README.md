# Rogelio Ruzcko Tobias

Personal academic and professional website built with the free, MIT-licensed
Hugo Blox Academic CV template and hosted with GitHub Pages.

## Local preview

The site requires Hugo Extended 0.161.1 or newer, Go, Node.js 22, and pnpm.

```sh
pnpm install
hugo server
```

## Production build

```sh
pnpm install
hugo --minify
pnpm run pagefind
```

The GitHub Actions workflow publishes the generated site to GitHub Pages.
