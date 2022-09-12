import React from "react";
import {Text, SafeAreaView, StyleSheet, TextInput} from "react-native";

const TwitterHandle = () => {
    const [text, onChangeText] = React.useState("@ScreenName");
  
    return (
      <SafeAreaView>
        <TextInput
          style={styles.input}
          onChangeText={onChangeText}
          value={text}
          />
        <Text> {text} </Text>
      </SafeAreaView>
    );
  };
  
  const styles = StyleSheet.create({
    input: {
      height: 40,
      margin: 12,
      borderWidth: 1,
      padding: 10,
    },
  });
  
  export default TwitterHandle;