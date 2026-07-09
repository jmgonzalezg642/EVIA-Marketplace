import React, { useState, useEffect } from 'react';
import { View, Text, StyleSheet, ScrollView, TouchableOpacity, ActivityIndicator } from 'react-native';
import { getProducts } from '../services/eviaService';

export default function HomeScreen({ navigation }) {
  const [products, setProducts] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    async function loadProducts() {
      try {
        setLoading(true);
        const data = await getProducts();
        setProducts(data);
        setError(null);
      } catch (err) {
        setError(err.message);
      } finally {
        setLoading(false);
      }
    }
    loadProducts();
  }, []);

  if (loading) {
    return (
      <View style={styles.center}>
        <ActivityIndicator size="large" color="#0057B8" />
        <Text style={styles.loadingText}>Cargando vehículos...</Text>
      </View>
    );
  }

  if (error) {
    return (
      <View style={styles.center}>
        <Text style={styles.errorText}>Error: {error}</Text>
      </View>
    );
  }

  // Mostrar solo los primeros 2 vehículos en el home
  const availableVehicles = products.slice(0, 2);

  return (
    <ScrollView style={styles.container}>
      {/* Header */}
      <View style={styles.header}>
        <Text style={styles.logo}>Evia</Text>
      </View>

      {/* Search Bar */}
      <TouchableOpacity 
        style={styles.searchContainer}
        onPress={() => navigation.navigate('Catalog')}
      >
        <Text style={styles.searchText}>🔍 Search EVs...</Text>
      </TouchableOpacity>

      {/* Vehicle Cards - AHORA USAN LA API */}
      <View style={styles.section}>
        <Text style={styles.sectionTitle}>Disponibles ahora</Text>
        <ScrollView horizontal showsHorizontalScrollIndicator={false}>
          {availableVehicles.map((item) => (
            <View key={item.id} style={styles.card}>
              <Text style={styles.cardTitle}>{item.marca} {item.modelo}</Text>
              <Text style={styles.cardSubtitle}>
                ⚡ {item.autonomia_km} km • {item.tipo_vehiculo}
              </Text>
              <Text style={styles.cardPrice}>
                ${Number(item.precio).toLocaleString()} COP
              </Text>
              <Text style={styles.cardStatus}>
                {item.es_nuevo ? '🆕 Nuevo' : '🔄 Usado'}
              </Text>
            </View>
          ))}
        </ScrollView>
      </View>

      {/* Charging Stations (estáticas por ahora) */}
      <View style={styles.section}>
        <Text style={styles.sectionTitle}>Estaciones de carga</Text>
        <View style={styles.stationCard}>
          <Text style={styles.stationName}>GreenCharge Station</Text>
          <Text style={styles.stationInfo}>0.8 km • 6/8 available</Text>
          <Text style={styles.stationTags}>CCS2, Type2</Text>
        </View>
        <View style={styles.stationCard}>
          <Text style={styles.stationName}>Evia Power Hub</Text>
          <Text style={styles.stationInfo}>0.8 km • 6/8 available</Text>
          <Text style={styles.stationTags}>CCS2, Type2</Text>
        </View>
      </View>
    </ScrollView>
  );
}

const styles = StyleSheet.create({
  container: { flex: 1, backgroundColor: '#F5F9FF' },
  center: { flex: 1, justifyContent: 'center', alignItems: 'center', backgroundColor: '#F5F9FF' },
  loadingText: { marginTop: 12, fontSize: 16, color: '#526075' },
  errorText: { fontSize: 16, color: '#B91C1C', textAlign: 'center' },
  header: { padding: 20, paddingTop: 40, backgroundColor: '#0057B8' },
  logo: { fontSize: 28, fontWeight: 'bold', color: '#FFFFFF' },
  subtitle: { fontSize: 16, color: '#FFFFFF', opacity: 0.9 },
  searchContainer: {
    margin: 16,
    padding: 14,
    backgroundColor: '#FFFFFF',
    borderRadius: 12,
    shadowColor: '#000',
    shadowOpacity: 0.1,
    shadowOffset: { width: 0, height: 2 },
    shadowRadius: 4,
    elevation: 2,
  },
  searchText: { color: '#94A3B8', fontSize: 16 },
  section: { paddingHorizontal: 16, marginBottom: 20 },
  sectionTitle: { fontSize: 18, fontWeight: 'bold', color: '#172033', marginBottom: 12 },
  card: {
    backgroundColor: '#FFFFFF',
    borderRadius: 12,
    padding: 16,
    marginRight: 12,
    width: 180,
    shadowColor: '#000',
    shadowOpacity: 0.08,
    shadowOffset: { width: 0, height: 2 },
    shadowRadius: 4,
    elevation: 2,
  },
  cardTitle: { fontSize: 16, fontWeight: 'bold', color: '#172033' },
  cardSubtitle: { fontSize: 12, color: '#526075', marginVertical: 4 },
  cardPrice: { fontSize: 15, fontWeight: 'bold', color: '#0057B8' },
  cardStatus: { fontSize: 12, fontWeight: '600', color: '#166534', marginTop: 4 },
  stationCard: {
    backgroundColor: '#FFFFFF',
    borderRadius: 12,
    padding: 16,
    marginBottom: 10,
    shadowColor: '#000',
    shadowOpacity: 0.05,
    shadowOffset: { width: 0, height: 2 },
    shadowRadius: 4,
    elevation: 1,
  },
  stationName: { fontSize: 16, fontWeight: 'bold', color: '#172033' },
  stationInfo: { fontSize: 14, color: '#526075', marginVertical: 2 },
  stationTags: { fontSize: 12, color: '#0057B8', fontWeight: '600' },
});