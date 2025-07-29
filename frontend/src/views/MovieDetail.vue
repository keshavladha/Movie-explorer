<template>
  <div>
    <!-- Loading State -->
    <div v-if="store.loading" class="text-center py-12">
      <div class="inline-block animate-spin rounded-full h-8 w-8 border-b-2 border-primary-600"></div>
      <p class="mt-2 text-gray-600">Loading movie details...</p>
    </div>

    <!-- Error State -->
    <div v-else-if="store.error" class="bg-red-50 border border-red-200 rounded-md p-4">
      <div class="flex">
        <div class="ml-3">
          <h3 class="text-sm font-medium text-red-800">Error loading movie</h3>
          <div class="mt-2 text-sm text-red-700">
            <p>{{ store.error }}</p>
          </div>
          <div class="mt-4">
            <router-link to="/" class="btn-primary">
              Back to Movies
            </router-link>
          </div>
        </div>
      </div>
    </div>

    <!-- Movie Details -->
    <div v-else-if="store.currentMovie" class="bg-white rounded-lg shadow-lg overflow-hidden">
      <!-- Header -->
      <div class="bg-primary-600 text-white p-8">
        <div class="flex justify-between items-start">
          <div>
            <h1 class="text-4xl font-bold mb-2">{{ store.currentMovie.title }}</h1>
            <p class="text-xl text-primary-100 mb-4">{{ store.currentMovie.release_year }}</p>
            <div class="flex items-center space-x-4 text-primary-100">
              <span v-if="store.currentMovie.duration">{{ store.currentMovie.duration }} minutes</span>
            </div>
          </div>
          <router-link to="/" class="btn-secondary">
            ← Back to Movies
          </router-link>
        </div>
      </div>

      <!-- Content -->
      <div class="p-8">
        <div class="grid grid-cols-1 lg:grid-cols-3 gap-8">
          <!-- Main Content -->
          <div class="lg:col-span-2">
            <!-- Synopsis -->
            <div class="mb-8">
              <h2 class="text-2xl font-bold text-gray-900 mb-4">Synopsis</h2>
              <p class="text-gray-700 leading-relaxed">
                {{ store.currentMovie.synopsis || 'No synopsis available.' }}
              </p>
            </div>

            <!-- Cast -->
            <div class="mb-8">
              <h2 class="text-2xl font-bold text-gray-900 mb-4">Cast</h2>
              <div v-if="store.currentMovie.actors.length > 0" class="grid grid-cols-1 sm:grid-cols-2 gap-4">
                <div 
                  v-for="actor in store.currentMovie.actors" 
                  :key="actor.id"
                  class="bg-gray-50 rounded-lg p-4 hover:bg-gray-100 transition-colors"
                >
                  <router-link 
                    :to="`/actor/${actor.id}`"
                    class="block"
                  >
                    <h3 class="font-semibold text-gray-900 hover:text-primary-600">
                      {{ actor.name }}
                    </h3>
                    <p class="text-sm text-gray-600" v-if="actor.birth_year">
                      Born: {{ actor.birth_year }}
                    </p>
                  </router-link>
                </div>
              </div>
              <p v-else class="text-gray-600">No cast information available.</p>
            </div>
          </div>

          <!-- Sidebar -->
          <div class="lg:col-span-1">
            <!-- Director -->
            <div class="bg-gray-50 rounded-lg p-6 mb-6">
              <h3 class="text-lg font-semibold text-gray-900 mb-3">Director</h3>
              <div v-if="store.currentMovie.director">
                <router-link 
                  :to="`/director/${store.currentMovie.director.id}`"
                  class="block hover:bg-gray-100 rounded p-2 -m-2 transition-colors"
                >
                  <h4 class="font-medium text-gray-900 hover:text-primary-600">
                    {{ store.currentMovie.director.name }}
                  </h4>
                  <p class="text-sm text-gray-600" v-if="store.currentMovie.director.birth_year">
                    Born: {{ store.currentMovie.director.birth_year }}
                  </p>
                </router-link>
              </div>
              <p v-else class="text-gray-600">No director information available.</p>
            </div>

            <!-- Genres -->
            <div class="bg-gray-50 rounded-lg p-6">
              <h3 class="text-lg font-semibold text-gray-900 mb-3">Genres</h3>
              <div v-if="store.currentMovie.genres.length > 0" class="space-y-2">
                <span 
                  v-for="genre in store.currentMovie.genres" 
                  :key="genre.id"
                  class="inline-block bg-primary-100 text-primary-800 px-3 py-1 rounded-full text-sm font-medium mr-2 mb-2"
                >
                  {{ genre.name }}
                </span>
              </div>
              <p v-else class="text-gray-600">No genre information available.</p>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { onMounted, watch } from 'vue'
import { useMovieStore } from '@/stores'

const props = defineProps<{
  id: string
}>()

const store = useMovieStore()

const loadMovie = () => {
  const movieId = parseInt(props.id)
  if (!isNaN(movieId)) {
    store.fetchMovie(movieId)
  }
}

onMounted(() => {
  loadMovie()
})

watch(() => props.id, () => {
  loadMovie()
})
</script> 