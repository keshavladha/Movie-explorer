<template>
  <div>
    <!-- Hero Section -->
    <div class="bg-primary-600 text-white py-12 px-6 rounded-lg mb-8">
      <div class="text-center">
        <h1 class="text-4xl font-bold mb-4">Welcome to Movie Explorer</h1>
        <p class="text-xl text-primary-100">
          Discover amazing movies, explore talented actors, and learn about brilliant directors
        </p>
      </div>
    </div>

    <!-- Filters -->
    <MovieFilters 
      :genres="store.genres"
      :directors="store.directors"
      :actors="store.actors"
      :release-years="store.uniqueReleaseYears"
      @filters-changed="handleFiltersChanged"
    />

    <!-- Loading State -->
    <div v-if="store.loading" class="text-center py-8">
      <div class="inline-block animate-spin rounded-full h-8 w-8 border-b-2 border-primary-600"></div>
      <p class="mt-2 text-gray-600">Loading movies...</p>
    </div>

    <!-- Error State -->
    <div v-else-if="store.error" class="bg-red-50 border border-red-200 rounded-md p-4 mb-6">
      <div class="flex">
        <div class="ml-3">
          <h3 class="text-sm font-medium text-red-800">
            Error loading data
          </h3>
          <div class="mt-2 text-sm text-red-700">
            <p>{{ store.error }}</p>
          </div>
          <div class="mt-4">
            <button @click="loadData" class="btn-primary">
              Try Again
            </button>
          </div>
        </div>
      </div>
    </div>

    <!-- Movies Grid -->
    <div v-else>
      <div class="flex justify-between items-center mb-6">
        <h2 class="text-2xl font-bold text-gray-900">
          Movies
          <span class="text-lg font-normal text-gray-600">
            ({{ store.moviesCount }} found)
          </span>
        </h2>
      </div>

      <!-- No Results -->
      <div v-if="store.movies.length === 0" class="text-center py-12">
        <div class="text-gray-400 text-6xl mb-4">🎬</div>
        <h3 class="text-lg font-medium text-gray-900 mb-2">No movies found</h3>
        <p class="text-gray-600">Try adjusting your filters to see more results.</p>
      </div>

      <!-- Movies Grid -->
      <div v-else class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
        <MovieCard 
          v-for="movie in store.movies" 
          :key="movie.id" 
          :movie="movie" 
        />
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { onMounted } from 'vue'
import { useMovieStore } from '@/stores'
import MovieCard from '@/components/MovieCard.vue'
import MovieFilters from '@/components/MovieFilters.vue'
import type { FilterOptions } from '@/types'

const store = useMovieStore()

const loadData = async () => {
  await Promise.all([
    store.fetchMovies(),
    store.fetchGenres(),
    store.fetchDirectors(),
    store.fetchActors()
  ])
}

const handleFiltersChanged = (filters: FilterOptions) => {
  store.fetchMovies(filters)
}

onMounted(() => {
  loadData()
})
</script> 