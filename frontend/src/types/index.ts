export interface Genre {
  id: number
  name: string
  description?: string
}

export interface Actor {
  id: number
  name: string
  birth_year?: number
  bio?: string
  movies?: MovieSummary[]
}

export interface Director {
  id: number
  name: string
  birth_year?: number
  bio?: string
  movies?: MovieSummary[]
}

export interface MovieSummary {
  id: number
  title: string
  release_year: number
  synopsis?: string
  duration?: number
  director?: Director
}

export interface Movie extends MovieSummary {
  actors: Actor[]
  genres: Genre[]
}

export interface FilterOptions {
  genre_id?: number
  director_id?: number
  actor_id?: number
  release_year?: number
} 