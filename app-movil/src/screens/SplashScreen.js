import React, { useEffect } from 'react';
import { View, Text, StyleSheet, Image, TouchableOpacity } from 'react-native';

export default function SplashScreen({ navigation }) {
  useEffect(() => {
    // Auto-navegar después de 3 segundos (opcional)
    // const timer = setTimeout(() => navigation.replace('Login'), 3000);
    // return () => clearTimeout(timer);
  }, []);

  return (
    <View style={styles.container}>
      <View style={styles.content}>
        <Text style={styles.logo}>⚡</Text>
        <Text style={styles.title}>EVIA</Text>
        <Text style={styles.subtitle}>Conduciendo hacia el futuro</Text>
        <Text style={styles.version}>Vehículos 100% eléctricos</Text>
      </View>

      <TouchableOpacity 
        style={styles.button} 
        onPress={() => navigation.replace('Login')}
      >
        <Text style={styles.buttonText}>Comenzar</Text>
      </TouchableOpacity>
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#0057B8',
    justifyContent: 'center',
    alignItems: 'center',
    padding: 24,
  },
  content: {
    alignItems: 'center',
    flex: 1,
    justifyContent: 'center',
  },
  logo: {
    fontSize: 80,
    marginBottom: 10,
  },
  title: {
    fontSize: 48,
    fontWeight: 'bold',
    color: '#FFFFFF',
    letterSpacing: 2,
  },
  subtitle: {
    fontSize: 18,
    color: '#FFFFFF',
    opacity: 0.9,
    marginTop: 8,
  },
  version: {
    fontSize: 14,
    color: '#FFFFFF',
    opacity: 0.7,
    marginTop: 20,
  },
  button: {
    backgroundColor: '#FFFFFF',
    borderRadius: 30,
    paddingVertical: 16,
    paddingHorizontal: 60,
    marginBottom: 40,
    shadowColor: '#000',
    shadowOpacity: 0.2,
    shadowOffset: { width: 0, height: 4 },
    shadowRadius: 8,
    elevation: 5,
  },
  buttonText: {
    fontSize: 18,
    fontWeight: 'bold',
    color: '#0057B8',
  },
});