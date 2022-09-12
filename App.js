import { StatusBar } from 'expo-status-bar';
import { StyleSheet, Text, View } from 'react-native';
import TwitterHandle from './TwitterHandle.js';

export default function App() {
  return (
    <View style={styles.container}>
      <Text>Enter A Twitter Handle</Text>
      <StatusBar style="auto" />
      <TwitterHandle></TwitterHandle>
    </View>
  );
}


const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#eff',
    alignItems: 'center',
    justifyContent: 'center',
  },
});
